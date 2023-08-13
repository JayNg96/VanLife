export async function getVanApi() {
    const response = await fetch('/api/vans')
    if (!response.ok) {
        // eslint-disable-next-line
        throw {
            message: "Failed to fetch vans", 
            statusText: response.statusText,
            status: response.status
        }
    }
    const data = await response.json()
    return data.vans
}