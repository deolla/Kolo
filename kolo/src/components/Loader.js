import React from "react";
import { View, StyleSheet, useWindowDimensions, ActivityIndicator, Text } from "react-native";
import COLORS from "./colours";

const Loader = ({visible = false}) => {
    const {height, width} = useWindowDimensions();
        return (
            visible && (
                <View style={[style.container, {height, width}]}>
                    <View style={style.loader}>
                        <ActivityIndicator size="large" color={COLORS.blue} />
                        <Text style={[style.loadingText]}>Loading..</Text>
                    </View>
                </View>
            )
        );
    };


const style = StyleSheet.create({
    container: {
        position: "absolute",
        zIndex: 10,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        justifyContent: 'center',
    },
    loader: {
        height: 60,
        backgroundColor: COLORS.white,
        marginHorizontal: 50,
        borderRadius: 5,
        flexDirection: "row",
        alignContent: "center",
        paddingHorizontal: 20,
    },
    loadingText: {
        marginLeft: 15,
        // Takes up the remaining space
        fontSize: 16,
    },
});

export default Loader;
