import React from "react";
import { View, Text, StyleSheet } from "react-native";
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import COLORS from "./colours";
import { TextInput } from "react-native-gesture-handler";
import { err } from "react-native-svg";



const Input = ({
    label, 
    iconName,
    error,
    password,
    onFocus = () => {},
    ...props 
}) => {
    const [isFocused, setIsFocused] = React.useState(false);
    const [hidePasswords, setHidePasswords] = React.useState(password);
    return (
        <View style={{marginBottom: 20}} >
        <Text style={style.label}>
            {label}
        </Text>
        <View style={[style.InputContainer, 
            {
                borderColor: error
                    ? COLORS.red:isFocused
                    ? COLORS.dark_blue : COLORS.light,
            },
       ]}>
            <Icon 
                name={iconName}
                style={{fontSize: 22, color: COLORS.dark_blue, marginRight: 10}} />
                <TextInput 
                    secureTextEntry={hidePasswords}
                    autoCorrect={false}
                    onFocus={() => {
                        onFocus();
                        setIsFocused(true); 
                }}
                onBlur={() => {
                    setIsFocused(false);
                }}
                style={{color: COLORS.dark_blue, flex: 1}} {...props} 
            />
            {password && (
                <Icon 
                    onPress={() => setHidePasswords(!hidePasswords)}
                    style={{fontSize: 22, color: COLORS.dark_blue }}
                    name={hidePasswords ? "eye-outline" : "eye-off-outline"}
                />
            )}
            </View>
        {error && (
            <Text style={{color: COLORS.red, fontSize: 12, marginTop: 7}}>
                {error}
            </Text>
        )}
    </View>
    );
};

const style = StyleSheet.create({
    label: {
        marginVertical: 5,
        fontSize: 14,
        color: COLORS.grey,
    },
    InputContainer: {
        height: 45,
        backgroundColor: COLORS.light,
        flexDirection: 'row',
        paddingHorizontal: 10,
        borderWidth: 0.3,
        alignItems: 'center',
    },
});


export default Input;