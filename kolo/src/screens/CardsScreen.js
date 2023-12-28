import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default CardsScreen = () => {
    return (
        <View style={styles.container}>
        <Text>Cards Screen</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "center",
    },
});