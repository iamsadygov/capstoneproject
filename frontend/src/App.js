   //                                                       
 // ██████╗  ██████╗ ██╗  ██╗ ██████╗██╗  ██╗███████╗███╗   ██╗
// ██╔════╝ ██╔═══██╗██║ ██╔╝██╔════╝██║  ██║██╔════╝████╗  ██║
// ██║  ███╗██║   ██║█████╔╝ ██║     ███████║█████╗  ██╔██╗ ██║
// ██║   ██║██║   ██║██╔═██╗ ██║     ██╔══██║██╔══╝  ██║╚██╗██║
// ╚██████╔╝╚██████╔╝██║  ██╗╚██████╗██║  ██║███████╗██║ ╚████║
 // ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
  //                                                       

import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import Layout from "./components/Layout/Layout";
import HomePage from "./components/HomePage/HomePage";
import RankingPage from "./components/RankingPage/RankingPage";
import Results from "./components/ResultsPage/Results";

function App() {
  const [, setSelectedBrand] = useState("All");

  return (
    <Router>
      <Layout onBrandSelect={setSelectedBrand}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/ranking" element={<RankingPage />} />
          <Route path="/results" element={<ResultsWrapper />} />
        </Routes>
      </Layout>
    </Router>
  );
}

const ResultsWrapper = () => {
  const location = useLocation();
  const { rankings, results } = location.state || { rankings: {}, results: [] };
  return <Results rankings={rankings} results={results} />;
};

export default App;
