import React from "react"
import { useOutletContext } from "react-router-dom";

export function HostVanPricing() {
    const currentVan = useOutletContext();
    console.log(currentVan)
    return (
        <>
            <p><b>${currentVan.price}</b>/day</p>
        </>
    )
}