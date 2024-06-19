package main

import "fmt"

type User string

type Document struct {
	Owner          string
	AllowedToRead  []string
	AllowedToWrite []string
	Data           string
	Deleted        bool
}

func (d *Document) Read(user string) (string, error) {

	if d.Deleted {
		return "", fmt.Errorf("Document does not exit")
	}

	if user == d.Owner {
		return d.Data, nil
	}

	for _, allowedUser := range d.AllowedToRead {
		if user == allowedUser {
			return d.Data, nil
		}
	}

	return "", fmt.Errorf("Not Allowed")
}

func (d *Document) Write(user string, userData string) error {
	if d.Deleted {
		return fmt.Errorf("Document does not exit")
	}

	if user == d.Owner {
		d.Data = userData
		return nil
	}
	for i, _ := range d.AllowedToWrite {
		if user == d.AllowedToWrite[i] {
			d.Data = userData
			return nil
		}
	}
	return fmt.Errorf("Not Allowed")
}

func (d *Document) AddReadAllowedUser(owner string, user string) error {
	if d.Deleted {
		return fmt.Errorf("Document does not exit")
	}

	if owner == d.Owner {
		d.AllowedToRead = append(d.AllowedToRead, user)
		return nil
	}
	return fmt.Errorf("Not Allowed")
}

func (d *Document) AddWriteAllowedUser(owner string, user string) error {
	if d.Deleted {
		return fmt.Errorf("Document does not exit")
	}

	if owner == d.Owner {
		d.AllowedToWrite = append(d.AllowedToWrite, user)
		return nil
	}
	return fmt.Errorf("Not Allowed")
}

func (d *Document) Delete(owner string) error {
	if d.Deleted {
		return fmt.Errorf("Document does not exit")
	}

	if owner == d.Owner {
		d.Deleted = true
		return nil
	}
	return fmt.Errorf("Not Allowed")
}

func MakeDocument(owner, data string) *Document {
	return &Document{
		Owner:          owner,
		Data:           data,
		AllowedToRead:  []string{},
		AllowedToWrite: []string{},
		Deleted:        false,
	}
}

func main() {

	doc := MakeDocument("dhawal", "lorem")

	str, err := doc.Read("dhawal")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(str) // lorem
	}

	err = doc.Write("dhawal", "ipsum")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("No Error")
	}

	str, err = doc.Read("sagar")
	if err != nil {
		fmt.Println(err) // not allowed
	} else {
		fmt.Println(str)
	}

	err = doc.AddReadAllowedUser("dhawal", "sagar")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("No Error") // no error
	}

	str, err = doc.Read("sagar")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(str) // ipsum
	}

	err = doc.Write("pramod", "lorem")
	if err != nil {
		fmt.Println(err) // not allowed
	} else {
		fmt.Println("No Error")
	}

	err = doc.AddWriteAllowedUser("dhawal", "pramod")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("No Error") //
	}

	err = doc.Write("pramod", "lorem")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("No Error") // allowed
	}

	err = doc.Delete("clark")
	if err != nil {
		fmt.Println(err) // not allowed
	} else {
		fmt.Println("No Error")
	}

	err = doc.Delete("dhawal") //  allowed
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Document Deleted")
	}

	str, err = doc.Read("sagar")
	if err != nil {
		fmt.Println(err) // not allowed
	} else {
		fmt.Println(str)
	}

	err = doc.AddReadAllowedUser("sagar", "clark")
	if err != nil {
		fmt.Println(err) // not allowed
	} else {
		fmt.Println("No Error")
	}

}
