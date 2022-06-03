import React, { useEffect } from "react";
import { createCustomEqual } from "fast-equals";
import { isLatLngLiteral } from "@googlemaps/typescript-guards";

const deepCompareEqualsForMaps = createCustomEqual(
    (deepEqual: any) => (a: any, b: any) => {
        if (
            isLatLngLiteral(a) ||
            a instanceof google.maps.LatLng ||
            isLatLngLiteral(b) ||
            b instanceof google.maps.LatLng
        ) {
            return new google.maps.LatLng(a).equals(new google.maps.LatLng(b));
        }

        // TODO extend to other types

        // use fast-equals for other objects
        return deepEqual(a, b);
    }
);

function useDeepCompareMemoize(value: any) {
    const ref = React.useRef();

    if (!deepCompareEqualsForMaps(value, ref.current)) {
        ref.current = value;
    }

    return ref.current;
}

function useDeepCompareEffectForMaps(
    callback: React.EffectCallback,
    dependencies: any[]
) {
    React.useEffect(callback, dependencies.map(useDeepCompareMemoize));
}

export function Marker(options: google.maps.MarkerOptions) {
    const [marker, setMarker] = React.useState<google.maps.Marker>();

    React.useEffect(() => {
        if (!marker) {
            setMarker(new google.maps.Marker());
        }

        // remove marker from map on unmount
        return () => {
            if (marker) {
                marker.setMap(null);
            }
        };
    }, [marker]);

    React.useEffect(() => {
        const image = require('../assets/store.png');

        if (marker) {
            marker.setOptions({
                ...options,
                icon: {
                    url: image,
                    scaledSize: new google.maps.Size(64, 64)
                }
            });
        }
    }, [marker, options]);

    return null;
};

interface IMapProps {
    center: google.maps.LatLngLiteral;
    zoom: number;
    onClick: (event: google.maps.MapMouseEvent) => void;
    onIdle: (event: google.maps.Map) => void;
    children: React.ReactNode;
}

export function Map(props: IMapProps) {

    const ref = React.useRef<HTMLDivElement>(null);
    const [map, setMap] = React.useState<google.maps.Map>();
    const { children, ...options } = props;

    useDeepCompareEffectForMaps(() => {
        if (map)
            map.setOptions(options);
    }, [map, options]);

    useEffect(() => {
        if (ref.current && !map) {
            setMap(new window.google.maps.Map(ref.current, {}));
        }
    }, [ref, map]);

    useEffect(() => {
        if (map) {

            ["click", "idle"].forEach((eventName) =>
                google.maps.event.clearListeners(map, eventName)
            );

            if (props.onIdle) {
                map.addListener('idle', () => props.onIdle(map));
            }

            if (props.onClick) {
                map.addListener('click', props.onClick);
            }

        }

    }, [map]);

    return (
        <>
            <div ref={ref} style={{ width: "90%", height: "70vh" }} />
            {React.Children.map(children, (child) => {
                if (React.isValidElement(child)) {
                    return React.cloneElement(child, { map });
                }
            })}

            <span className="text-info">- Click on the map to enable to form -</span>

        </>
    )
}