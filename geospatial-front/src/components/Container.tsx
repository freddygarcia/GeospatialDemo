import { Wrapper } from "@googlemaps/react-wrapper";
import { useStores } from "../hooks/useStores";
import { useMap } from "../hooks/useMap";
import { Form } from "./Form";
import { List } from "./List";
import { Map, Marker } from "./Map";


export function Container() {


    const { stores, addStore } = useStores();
    const { center, zoom, onMapClick, newMarker, setNewMarker, onIdle, selected, onSelectStore } = useMap();

    return (
        <div className="container">
            <section style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '0 10%' }} >
                <Form location={newMarker} setLocation={setNewMarker} onSubmit={addStore} selected={selected} />
                <List items={stores} onClick={onSelectStore} selected={selected} />
            </section>
            <section style={{ flex: 1 }}>
                <Wrapper apiKey={process.env.REACT_APP_GOOGLE_API_KEY as string}>
                    <Map center={center} zoom={zoom} onClick={onMapClick} onIdle={onIdle}>
                        {stores.map(store => (
                            <Marker key={store.id} position={store.location} />
                        ))}
                        <Marker position={newMarker} />
                    </Map>
                </Wrapper>
            </section>
        </div>
    )
}