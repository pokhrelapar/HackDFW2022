import axios from 'axios'
import React, {useState,useEffect} from 'react';

/*
    calling the flask api end point
*/

const baseURL = 'http://127.0.0.1:5000';

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(baseURL+ '/explain').then((response) => {
      setPost(response.data);
    });
  }, []);

  if (!post) return null;

  return (
    <div>{post['Introduction']}</div>
  );
}
