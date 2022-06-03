import { useEffect, useRef, useState } from "react";
import { ILatLng, IStore } from "../hooks/useStores";

interface IFormProps {
    onSubmit: (store: IStore) => Promise<void>;
    location: ILatLng | null;
    setLocation: (location: ILatLng | null) => void;
    selected: IStore | null;
}

export function Form(props: IFormProps) {
    const [name, setName] = useState('');
    const [addr, setAddress] = useState('');

    const disableIfNotLocation = props.location === null;

    const ref = useRef<HTMLInputElement>(null);

    const createStore = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const location = props.location as ILatLng;

        const newStore = {
            name,
            location,
            addr,
            notes: "",
            phone: 0,
            active: true,
            zipcode: 0
        }

        props.onSubmit(newStore).then(() => {
            setName('');
            setAddress('');
            props.setLocation(null);
        });
    }

    useEffect(() => {
        setName(props.selected?.name || '');
        setAddress(props.selected?.addr || '');
    }, [props.selected]);

    useEffect(() => {
        setName('');
        setAddress('');

        if (ref.current)
            ref.current.focus();
    }, [props.location]);

    return (
        <form style={{ flex: 1, flexDirection: 'column', display: 'flex' }} onSubmit={createStore}>
            <input readOnly={disableIfNotLocation} value={name} onChange={e => setName(e.target.value)} placeholder="Store name" ref={ref} />
            <input readOnly={disableIfNotLocation} value={addr} onChange={e => setAddress(e.target.value)} placeholder="Store address" />

            <pre>
                {props.location && JSON.stringify(props.location, null, 2)}
                {props.selected && JSON.stringify(props.selected?.location, null, 2)}
            </pre>

            <button disabled={disableIfNotLocation || !(name && addr)}>Save</button>
        </form>
    )
}