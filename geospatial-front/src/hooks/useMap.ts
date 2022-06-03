import { useCallback, useState } from "react";
import { ILatLng, IStore } from "./useStores";


export function useMap() {

    const [newMarker, setNewMarker] = useState<ILatLng | null>(null);
    const [selected, setSelected] = useState<IStore | null>(null);
    const [zoom, setZoom] = useState(11);
    const [center, setCenter] = useState<google.maps.LatLngLiteral>({
        lat: 38.9276614,
        lng: -77.0190404,
    });

    const onIdle = useCallback((m: google.maps.Map) => {
        if (m) {
            setZoom(m.getZoom()!);
            setCenter(m.getCenter()!.toJSON());
        }
    }, []);

    const onMapClick = useCallback((e: google.maps.MapMouseEvent) => {

        if (e.latLng) {
            const location = {
                lat: e.latLng.lat(),
                lng: e.latLng.lng(),
            };

            setZoom(11);
            setNewMarker(location);
            setSelected(null);
        }
    }, [])

    const onSelectStore = (store: IStore) => {
        setCenter(store.location);
        setZoom(15);
        setSelected(store);
        setNewMarker(null);
    }

    return {
        center,
        setCenter,
        selected,
        setSelected,
        zoom,
        setZoom,
        newMarker,
        setNewMarker,
        onIdle,
        onMapClick,
        onSelectStore
    }
}