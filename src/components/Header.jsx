import React from "react"
import { NavLink, Link } from 'react-router-dom'
import avatarIcon from '../assets/images/avatar-icon.png'

export function Header() {
    return (
        <header>
            <Link className="site-logo" to="/">#VanLife</Link>
            <nav>
                <NavLink className={({isActive}) => isActive ? "nav-selected" : ""} to="/host">Host</NavLink>
                <NavLink className={({isActive}) => isActive ? "nav-selected" : ""} to="/about">About</NavLink>
                <NavLink className={({isActive}) => isActive ? "nav-selected" : ""} to="/vans">Vans</NavLink>
                <Link to="login" className="login-link">
                    <img src={avatarIcon} className="login-icon" alt="login"/>
                </Link>
            </nav>
        </header>
    )
}