import React, { useState } from 'react';
import './Example.css';
import styled from "styled-components";
function Example()
{
    const Button = styled.button`
background-color: black;
color: white;
font-size: 20px;
padding: 10px 60px;
border-radius: 5px;
margin: 10px 0px;
cursor: pointer;
`;
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>You clicked {count} times</p>
            <div>
                <Button onClick={() => setCount(count + 1)}>
                    +
                </Button>
                <Button onClick={() => setCount(count - 1)}>
                    -
                </Button>
            </div>
        </div>
    );
}

export default Example;