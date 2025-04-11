import './App.css';
import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/items/').then((response) => {
      setData(response.data);
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        {data.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </header>
    </div>
  );
}

export default App;
