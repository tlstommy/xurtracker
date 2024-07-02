//REF


import React from 'react';

const DestinyData = ({ data }) => {
  return (
    <div>
      <h2>Destiny Data</h2>
      <p><strong>Location:</strong> {data.Location}</p>
      <p><strong>Planet:</strong> {data.Planet}</p>
      <p><strong>Landing Zone:</strong> {data["Landing Zone"]}</p>
      <p><strong>Week:</strong> {data.Week}</p>
      
      <h3>Exotics</h3>
      <ul>
        {Object.entries(data.Exotics).map(([key, value]) => (
          <li key={key}>
            <strong>{value.name}</strong> ({value.type})
          </li>
        ))}
      </ul>

      <h3>Legendaries</h3>
      <ul>
        {data.Legendaries["Legendary weapons"].map((weapon) => (
          <li key={weapon.itemHash}>
            <strong>{weapon.name}</strong> ({weapon.type})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DestinyData;
