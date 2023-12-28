import React from "react";
import { Text, View, ScrollView, Alert, Keyboard, SafeAreaView } from "react-native";
import AsyncStorage from  '@react-native-async-storage/async-storage';
import COLORS from "../components/colours";
import Button from '../components/Button';
import Loader from "../components/Loader";


import Input from "../components/input";

const LoginScreen = ({ navigation }) => {
  const [inputs, setInputs] = React.useState({
    email: "",
    fullname: "",
    username: "",
    phone: "",
    password: "",
    address: "",
  });
  const [errors, setErrors] = React.useState({})
  const [loading, setLoading] = React.useState(false);

  const validate = () => {
    Keyboard.dismiss();
    let valid = true;
    if (!inputs.email) {
      handleError("Please enter a valid email address", "email");
      valid = false;
    }

    if(!inputs.password) {
        valid = false;
      handleError("Please enter your password", "password");
    }

    if (valid) {
      login();
    }
  };
  
  const login = () => {
    setLoading(true);
    fetch('http://192.168.0.163:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(inputs),
    }).then((res) => res.json())
    .then((data) => {
      console.log("Server Response: ", data);
      setLoading(false);
      if (data.error) {
        Alert.alert("Error", data.error);
    } else {
      if (data.user && data.user !== null && data.user !== undefined) {
        try {
          AsyncStorage.setItem("user", JSON.stringify(data.user));
          Alert.alert("Success", data.message)
        } catch (error) {
          Alert.alert("Error", 'Unable to access Homepage');
        }
        Alert.alert("Success", data.message);
        navigation.navigate("DashBoard");
      }
    }
  })
  .catch((error) => {
    setLoading(false);
    Alert.alert("Error", "Unable to access login page");
    console.log(error);
  });
};


  const handleOnChange = (text, input) => {
    setInputs(prevState => ({...prevState, [input]: text}));
  };

  const handleError = (errorMessage, input) => {
    setErrors((prevState)=>({...prevState, [input] : errorMessage}))
  };

  return (
    <SafeAreaView style={{ backgroundColor: COLORS.WHITE, flex: 1 }}>
    <Loader visible={loading} />
      <ScrollView
        contentContainerStyle={{
          paddingTop: 50,
          paddingHorizontal: 20,
        }}>
        <Text style={{ color: "#000000", fontSize: 40, fontWeight: "bold" }}>
          Welcome 
        </Text>
        <Text style={{ color: "grey", fontSize: 18, marginVertical: 10 }}>
          Enter Your Details
        </Text>
        <View style={{marginVertical: 20}}>
          <Input 
            placeholder="Enter your email address"
            iconName="email-outline"
            label="Email"
            error={errors.email}
            onFocus={() => {
              handleError(null, "email");
            }}
            onChangeText = {text => handleOnChange(text, "email")}
            // error="Please enter a valid email address"
          />
          <Input 
            placeholder="Enter your password"
            iconName="lock-outline"
            label="Password"
            error={errors.password}
            onFocus={() => {
              handleError(null, "password");
            }}
            onChangeText = {text => handleOnChange(text, "password")}
            // error="Please enter a valid password"
            password
          />
          <Button title="Login" onPress={validate}/>
          <Text 
            onPress={() => navigation.navigate("Register")}
            style={{color: COLORS.black,
            textAlign: 'center',
            fontWeight: 'bold',
          }}>
          Don't have an account? Register now
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

export default LoginScreen;
