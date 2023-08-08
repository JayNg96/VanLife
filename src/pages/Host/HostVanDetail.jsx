import React from 'react'
import { useParams } from 'react-router-dom';

export function HostVanDetail() {

    const { id } = useParams()
    const [currentVan, setHostVan] = React.useState(null)

    React.useEffect(()=>{
        fetch(`/api/host/vans/${id}`)
            .then(res => res.json())
            .then(data => setHostVan(data.vans))
            // eslint-disable-next-line
    }, [])
    
    if(currentVan){
        console.log(currentVan.id)
    }
    
    return (
        <>
            {
                currentVan ?
                <div>
                    <img src={currentVan.imageUrl} width={150} alt="current van"/>
                    <h2>{currentVan.name}</h2>
                    <p>{currentVan.price}</p>
                    <p>{currentVan.type}</p>
                </div>
                :
                <h1>Loading...</h1>
            }
        </>
    )

};