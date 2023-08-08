import React from "react"
import { NavLink, Link } from 'react-router-dom'

export function Header() {
    return (
        <header>
            <Link className="site-logo" to="/">#VanLife</Link>
            <nav>
                <NavLink className={({isActive}) => isActive ? "nav-selected" : ""} to="/host">Host</NavLink>
                <NavLink className={({isActive}) => isActive ? "nav-selected" : ""} to="/about">About</NavLink>
                <NavLink className={({isActive}) => isActive ? "nav-selected" : ""} to="/vans">Vans</NavLink>
            </nav>
        </header>
    )
}