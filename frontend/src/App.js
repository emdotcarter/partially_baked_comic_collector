import logo from './logo.svg';
import './App.css';
import ComicList from './components/ComicList'
import { useState, useEffect } from 'react'

function App() {
  const [comics, setComics] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3001/api/1/comics', {
      'methods': 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(response => setComics(response))
      .catch(error => console.log(error))

  }, [])

  return (
/*  */


    <div className="App">
    <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      {/* <p>
        Edit <code>src/App.js</code> and save to reload.
      </p>
      <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        Learn React
      </a> */}
      <ComicList comics={comics} />
    </header>
    </div>
  );
}

export default App;
