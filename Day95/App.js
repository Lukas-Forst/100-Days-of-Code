import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

const App = () =>
{
  const [num, setNum] = useState(0);
  const [color, setCol] = useState(0);
  function randomNumberInRange(min, max)
  {
    // 👇️ get number between min (inclusive) and max (inclusive)
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  function generateNum()
  {
    var val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];
    let strin = "#";
    var max = val.length;
    var min = 0
    for (var i = 0; i < 6; i++)
    {
      let rand = Math.floor(Math.random() * (max - min)) + min;
      //console.log(rand, val[rand])
      strin += val[rand];

    }

    return strin
  }
  const handleClick = () =>
  {
    setNum(randomNumberInRange(1, 5000));
  };
  const genColor = () =>
  {
    setCol(generateNum());
  };

  return (
    <div>
      <h2>number is: {num}</h2>
      <button onClick={handleClick}>Generate random number</button>
      <button onClick={genColor}>Generate random number</button>
      <div id="some_box" style={{ backgroundColor: color }}>
      </div>
    </div>
  );
};

export default App;
