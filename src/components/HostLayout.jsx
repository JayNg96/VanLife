import React from "react"
import { Outlet } from 'react-router-dom'
import { NavLink } from 'react-router-dom'

export function HostLayout() {

    const currentlyActive = 
    {
        fontWeight: "bold",
        textDecoration: "underline",
        color: "#161616"
    }

    return (
        <>
            <nav className="host-nav">
                <NavLink to="/host" style={({isActive}) => isActive ? currentlyActive : null} end>Dashboard</NavLink>
                <NavLink to="/host/income" style={({isActive}) => isActive ? currentlyActive : null}>Income</NavLink>
                <NavLink to="/host/vans" style={({isActive}) => isActive ? currentlyActive : null}>Vans</NavLink>
                <NavLink to="/host/reviews" style={({isActive}) => isActive ? currentlyActive : null}>Reviews</NavLink>
            </nav>
            <Outlet/>
        </>   
    )
}