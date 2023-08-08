import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import { Home } from './pages/Home'
import { About } from './pages/About'
import { Vans } from './pages/Vans'
import { VanDetail } from './pages/VanDetail';
import { Layout } from './components/Layout'
import { Income } from './pages/Host/Income';
import { Dashboard } from './pages/Host/Dashboard';
import { Reviews } from './pages/Host/Reviews';
import { HostLayout } from './components/HostLayout';
import './index.css'
import "./server"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout/>}>
          <Route path="/" element={<Home/>}/>
          <Route path="/about" element={<About/>}/>
          <Route path="/vans" element={<Vans/>}/>
          <Route path="/vans/:id" element={<VanDetail/>}/>

          <Route element={<HostLayout />}>
            <Route path="/host/" element={<Dashboard />} />
            <Route path="/host/income" element={<Income />} />
            <Route path="/host/reviews" element={<Reviews />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(
    <App/>
);