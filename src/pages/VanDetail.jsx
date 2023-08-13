import React from "react"
import { useParams, Link, useLocation } from "react-router-dom"

export function VanDetail() {
    const params = useParams()
    const [van, setVan] = React.useState(null)
    const location = useLocation()

    React.useEffect(() => {
        fetch(`/api/vans/${params.id}`)
            .then(res => res.json())
            .then(data => setVan(data.vans))
    }, [params.id])

    return (
        <div className="van-detail-container">

            <Link
                to={`../${location.state.search}`}
                relative="path"
                className="back-button"
            >&larr; <span>Back to {location.state.type} vans</span></Link>


            <div className="van-detail">
                <img src={van.imageUrl} alt="van"/>
                <i className={`van-type ${van.type} selected`}>{van.type}</i>
                <h2>{van.name}</h2>
                <p className="van-price"><span>${van.price}</span>/day</p>
                <p>{van.description}</p>
                <button className="link-button">Rent this van</button>
            </div>

        </div>
    )
}