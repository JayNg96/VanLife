import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { Home } from './pages/Home'
import { About } from './pages/About'
import { Vans } from './pages/Vans'
import { VanDetail } from './pages/VanDetail';
import { Layout } from './components/Layout'
import { Income } from './pages/Host/Income';
import { Dashboard } from './pages/Host/Dashboard';
import { Reviews } from './pages/Host/Reviews';
import { HostLayout } from './components/HostLayout';
import { HostVanDetail } from './pages/Host/HostVanDetail';
import { HostVanInfo } from './pages/Host/HostVanInfo';
import { HostVanPricing } from './pages/Host/HostVanPricing';
import { HostVanPhotos } from './pages/Host/HostVanPhotos';
import { HostVans } from './pages/Host/HostVans';
import { NotFound } from './pages/NotFound';

import './index.css'
import "./server"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home/>}/>
          <Route path="about" element={<About/>}/>
          <Route path="vans" element={<Vans/>}/>
          <Route path="vans/:id" element={<VanDetail/>}/>

          <Route path="/host" element={<HostLayout />}>
            <Route index element={<Dashboard />} />
            <Route path="income" element={<Income />} />
            <Route path="reviews" element={<Reviews />} />
            <Route path="vans" element={<HostVans />} />
            <Route path="vans/:id" element={<HostVanDetail />}>
              <Route index element={<HostVanInfo />} />
              <Route path="pricing" element={<HostVanPricing />} />
              <Route path="photos" element={<HostVanPhotos />} />
            </Route>
          </Route>
          <Route path="*" element={<NotFound />}/>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(
    <App/>
);