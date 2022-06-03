import { useEffect, useState } from "react";


export interface ILatLng {
    lat: number;
    lng: number;
}
export interface IStore {
    id?: string;
    name: string;
    addr: string;
    phone: number;
    notes: string;
    active: boolean;
    zipcode: number;
    location: ILatLng;
}

export function useStores() {

    const [stores, setStores] = useState<IStore[]>([]);
    const API_URL = process.env.REACT_APP_API_URL;

    const addStore = (store: IStore) => {
        return fetch(`${API_URL}/stores/`, {
            method: 'POST',
            body: JSON.stringify(store),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then((res) => res.json())
            .then((data) => {
                setStores([...stores, data]);
            })
    }

    useEffect(() => {
        fetch(`${API_URL}/stores/`)
            .then(response => response.json())
            .then(data => setStores(data));
    }, []);

    return {
        stores,
        addStore
    }

}