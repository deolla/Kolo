import React from 'react';
import styled from 'styled-components';
import { Fontisto, MaterialIcons } from "@expo/vector-icons";

import Text from '../components/Text';
import { StatusBar } from 'expo-status-bar';


const TouchScreen = ({ navigation }) => {
    const handleThumbprintAuth = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/fingerprint_auth', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    thumbprint_data: 'biometric_data',
                }),
            });
            if (response.status === 200) {
                const result = await response.json();
                console.log(result.message);
            }else {
                console.error('Thumbprint authentication failed');
            }
        } catch (err) {
            console.err('Error during thumbprint authentication:', err);
        }
    };
    return (
    <Container>
        <Text center heavy title color="#964ff0" margin='32px 0 0 0' >
            Kolo
        </Text>

        <Touch onLongPress={() => navigation.navigate("Tabs")} delayPressIn={0}>
            <StyledCircle bgColor="#1e1e1e">
                <StyledCircle bgColor="#5196f405">
                    <StyledCircle bgColor="#5196f418">
                        <StyledCircle bgColor="#5196f430">
                            <TouchButton>
                                <MaterialIcons name="fingerprint" size={64} color="#ffffff" />
                            </TouchButton>
                        </StyledCircle>
                    </StyledCircle>
                </StyledCircle>
            </StyledCircle>
        </Touch>

        <Text center heavy large>Touch ID sensor</Text>
        <Text center bold margin="16px 0 0 0" color="#9c9c9f" >
            Touch the fingerprint sensor to log-in to your account</Text>
        
        <PinAccess onPress={() => navigation.navigate("Pin")} delayPressIn={0}>
            <Fontisto name="locked" color="#964ff0" size={18} />
            <Text bold margin="16px 0 0 0" color="#9c9c9f" >
                Enter Access PIN</Text>
        </PinAccess>

        <StatusBar barstyle="light-content"/>

    </Container>
    );
};

const Container = styled.SafeAreaView`
    flex: 1;
    background-color: #1e1e1e;
`;


const Touch = styled.TouchableOpacity`
    flex: 1;
    alignItems: center;
    justifyContent: center;

`

const StyledCircle = styled.View`
    background-color: ${props => props.bgColor};
    padding: 32px;
    border-radius: 999px;
`;

const TouchButton = styled.View`
    background-color: #5196f4;
    padding: 8px;
    border-radius: 100px;
`;

const PinAccess = styled.TouchableOpacity`
    margin-top: 16px;
    padding: 16px;
    alignItems: center;
    justifyContent: center;
`;

// const StatusBar = styled.StatusBar``;

export default TouchScreen;
