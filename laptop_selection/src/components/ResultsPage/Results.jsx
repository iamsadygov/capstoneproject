import React from "react";
import { useLocation } from "react-router-dom";
import "./Results.css";

const ResultsPage = () => {
  const location = useLocation();
  const { rankings, results } = location.state || { rankings: {}, results: [] };

  return (
    <div className="results-container">
      <div className="user-rankings">
        <h2>My Ranking:</h2>
        {Object.entries(rankings).map(([feature, value]) => (
          <div className="ranking-row" key={feature}>
            <span className="ranking-label">{feature.replace("_", " ")}:</span>
            <span className="ranking-value">{value}</span>
          </div>
        ))}
      </div>

      <div className="recommendation-panel">
  <h2>Best Recommendations For You:</h2>
  {results.length === 0 ? (
    <p>(Laptop cards or results will be shown here soon...)</p>
  ) : (
    <div className="results-grid">
      {results.map((laptop, index) => (
       <div key={index} className="laptop-card">
       <h3>{laptop["Laptop Name"]}</h3>
       <ul className="laptop-specs">
         <li>CPU: {laptop["CPU"]}</li>
         <li>GPU: {laptop["Graphic Card"]}</li>
         <li>RAM: {laptop["RAM"]} GB</li>
         <li>Storage: {laptop["Storage"]} GB</li>
         <li>Screen: {laptop["Screen Size"]} in</li>
         <li>OS: {laptop["Operating System"]}</li>
         <li>Brand: {laptop["Brand"]}</li>
         <li>Color: {laptop["Color"]}</li>
         <li>Weight: {laptop["Weight"]} kg</li>
         <li>Memory Speed: {laptop["Memory Speed"]} MHz</li>
         <li>Price: {laptop["Price"]} ₺</li>
       </ul>
       <strong>Correctness Score: {laptop["Correctness Score (%)"]}%</strong>
     </div>
      ))}
    </div>
  )}
</div>
    </div>
  );
};

export default ResultsPage;