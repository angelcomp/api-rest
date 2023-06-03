import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:5000/node'; // URL da API que você deseja fazer a requisição

const Node = () => {
  const [data, setData] = useState(null);

    const fetchData = async () => {
        try {
            const response = await axios.get(API_URL);  
            console.log(response.data)
            setData(response.data);
        } catch (error) {
            console.error('Erro ao fazer a requisição:', error);  
        }  
    };

    useEffect(() => {
        // Start the interval when the component mounts
        const interval = setInterval(() => {
        // Code to be executed at each interval
        fetchData();
        }, 5000); // Interval of 1 second

        // Clean up the interval when the component unmounts
        return () => {
        clearInterval(interval);
        };
    }, [data]);

  return (
    <>
      {data ? (
        <p>
          <p>Node:</p>
          {data.map((item) => (
            <div key={item.registration}>{item.name + " - " + item.registration }</div>
          ))}
        </p>
      ) : (
        <p>Carregando dados do server Node...</p>
      )}
    </>
  );
};

export default Node;
