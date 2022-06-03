import { IStore } from "../hooks/useStores";

interface IListProps {
    items: IStore[];
    onClick: (store: IStore) => void;
    selected: IStore | null;
}

export function List(props: IListProps) {
    const { items, onClick, selected } = props;

    return (
        <div className="list">
            <ul>
                {items.slice(0).reverse().map((store, index) => (
                    <li key={index} className={selected?.id === store.id ? 'selected' : ''}>
                        <div className="details" onClick={() => onClick(store)}>
                            <span className="name">{store.name}</span>
                            <span className="addr">{store.addr}</span>
                        </div>
                        <a href={"tel:" + store.phone} className='phone'>
                            <img alt={store.name} src={require('../assets/phone.png')} width={16} />
                        </a>
                    </li>
                ))}
            </ul>
        </div >
    )

}