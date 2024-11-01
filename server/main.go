package main

import (
    "fmt"
    "log"
    "net/http"
	// read environment variables
	"os"
    "github.com/gorilla/mux"
	"io/ioutil"
)

// return a response on "/"
func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World")
}

// get response from another service when a request is made to "/service" on port 6000
func ServiceHandler(w http.ResponseWriter, r *http.Request) {
	// make a request to the service
	resp, err := http.Get("http://localhost:6000")
	if err != nil {
		http.Error(w, err.Error(), http.StatusServiceUnavailable)
		return
	}
	defer resp.Body.Close()
	// read the response from the service
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusServiceUnavailable)
		return
	}
	// write the response to the client
	w.Write(body)
}

func main() {
	r := mux.NewRouter()
	port := os.Getenv("PORT")
	if port == "" {
		fmt.Println("PORT is not set")
		port = "8080"
	}
	r.HandleFunc("/", HomeHandler)
	http.Handle("/", r)
	http.HandleFunc("/service", ServiceHandler)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
