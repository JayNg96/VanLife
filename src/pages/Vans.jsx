import { Link, useSearchParams } from "react-router-dom"
import React from 'react'
import { getVanApi } from "../api"

export function Vans() {
    // eslint-disable-next-line
    const [searchParams, setSearchParams] = useSearchParams()
    const [vans, setVans] = React.useState([])
    // eslint-disable-next-line
    const [loading, setLoading] = React.useState(false)
    const [error, setError] = React.useState(null)
    const typeFilter = searchParams.get("type")

    React.useEffect(() => {
        async function loadVanApi() {
            setLoading(true)
            try { 
                const data = await getVanApi()
                setVans(data)
            } catch(err) {
                setError(err)
            } finally {
                setLoading(false)
            }
            setLoading(false)
        }

        loadVanApi()
    }, [])

    const displayedVans = typeFilter ? vans.filter(van => van.type === typeFilter) : vans

    const vanElements = displayedVans.map(van => (
        <div key={van.id} className="van-tile">
            <Link 
                to={van.id}
                state={{ search: `?${searchParams.toString()}`, type: typeFilter }}
            >
                <img src={van.imageUrl} alt="van"/>
                <div className="van-info">
                    <h3>{van.name}</h3>
                    <p>${van.price}<span>/day</span></p>
                </div>
                <i className={`van-type ${van.type} selected`}>{van.type}</i>
            </Link>
        </div>
    ))
     
    if(loading){
        return <h1 className="loading-text">Loading...</h1>
    }

    if(error){
        return <h1 className="loading-text"><h1>There was an error: {error.message}</h1></h1>
    }

    return (
        <div className="van-list-container">
            <h1>Explore our van options</h1>
            <div className="van-list-filter-buttons">
                <button 
                    onClick={() => setSearchParams({type: "simple"})}
                    className="van-type simple"
                >Simple</button>
                <button 
                    onClick={() => setSearchParams({type: "luxury"})}
                    className="van-type luxury"
                >Luxury</button>
                <button 
                    onClick={() => setSearchParams({type: "rugged"})}
                    className="van-type rugged"
                >Rugged</button>
                { typeFilter && 
                    <button 
                        onClick={() => setSearchParams({})}
                        className="van-type clear-filters"
                    >Clear filter</button>
                }

            </div>
            <div className="van-list">
                {vanElements}
            </div>
        </div>
    )
}