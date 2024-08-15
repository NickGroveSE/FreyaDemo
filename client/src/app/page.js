'use client'

import Image from "next/image";
import styles from "./page.module.css";
import { useState, useEffect } from 'react';

export default function Home() {

  // const [products, setProducts] = useState([])

  useEffect(() => {
    fetch("http://localhost:8080/api/products")
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
    })
  }, [])

  const addItem = async () => {
    fetch("http://localhost:8080/api/add", {
      method: "POST",
      body: JSON.stringify({
        data: "new random product"
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then((response) => response.json())
      .then((json) => console.log(json));
  }

  return (
    <div>
      <h1>Welcome to Freya's Initial Build</h1>
      <div>
        <button onClick={() => addItem()}>Add</button>
      </div>
      {/* <div id="items"></div> */}
    </div>
  );
}
