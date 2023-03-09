import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header";
import Home from "./components/Home/Home";
import Product from "./components/Product/Product";
// import "./assets/css/plugins/bootstrap.min.css";
import "./style.scss";
import './Media.scss'
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/product/:idx" element={<Product/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
