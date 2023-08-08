import React from "react"
import { Outlet } from 'react-router-dom'
import { Link } from 'react-router-dom'

export function HostLayout() {
    return (
        <>
            <Link to="/host">Dashboard</Link>
            <Link to="/host/income">Income</Link>
            <Link to="/host/reviews">Reviews</Link>
            <Outlet/>
        </>   
    )
}