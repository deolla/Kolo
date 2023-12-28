import React from "react";
import { Text, TouchableOpacity } from "react-native";
import COLORS from "./colours";

const Button = ({ title, onPress = () => {} }) => {
  return (
    <TouchableOpacity
      activeOpacity={0.7} onPress={onPress}
      style={{
        height: 55,
        width: "100%",
        backgroundColor: COLORS.blue,
        justifyContent: "center",
        alignItems: "center",
        marginVertical: 20,
      }}>
      <Text style={{ color: COLORS.white, fontWeight: "bold", fontSize: 18 }}>
        {title}
      </Text>
    </TouchableOpacity>
  );
};

export default Button;
