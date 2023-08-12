import React from "react"
import { useOutletContext } from "react-router-dom";

export function HostVanPhotos() {
    const currentVan = useOutletContext();
    console.log(currentVan)
    return (
        <img src={currentVan.imageUrl} alt="van" style={{width: 250}}/>
    )
}