import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default SendRequestScreen = () => {
    return (
        <View style={styles.container}>
        <Text>Send Request Screen</Text>
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