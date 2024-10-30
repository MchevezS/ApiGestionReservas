import React from "react";
import { BrowSerRoutes as Router, Routes, Route} from 'react-router-dom';

import Home from "../pages/Home";

const Routing = () => {
    return (
        <Router>
            <Routes>
                <Route path="/Home" element={<Home/>} />
            </Routes>
        </Router>
    );
};

export default Routing;
