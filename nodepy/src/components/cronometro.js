import React, { useState, useEffect } from 'react';

const Cronometro = () => {
  const [segundos, setSegundos] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setSegundos((prevSegundos) => prevSegundos + 1);
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, []);

  return <div>{segundos} segundos</div>;
};

export default Cronometro;
