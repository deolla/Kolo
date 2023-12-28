import React from "react";
import { Alert, Keyboard, SafeAreaView } from "react-native";
import { Text, View, ScrollView } from "react-native";
import AsyncStorage from  '@react-native-async-storage/async-storage';
import COLORS from "../components/colours";
import Button from '../components/Button';
import Loader from "../components/Loader";


import Input from "../components/input";

const RegisterScreen = ({ navigation }) => {
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
    } else if (!inputs.email.match(/\S+@\S+\.\S+/)) {
      handleError("Please enter a valid email address", "email");
    }

    if(!inputs.fullname) {
      valid = false;
      handleError("Please enter your fullname", "fullname");
     
    }

    if(!inputs.username) {
      valid = false;
      handleError("Please enter your username", "username");
    
    }
    
    if(!inputs.phone) {
      valid = false;
      handleError("Please enter your phone number", "phone");
      
    }

    if(!inputs.address) {
      valid = false;
      handleError("Please enter your address", "address");
    
    }

    if(!inputs.password) {
      valid = false;
      handleError("Please enter your password", "password");

    } else if (inputs.password.length < 8) {
      handleError("Password must be at least 8 characters", "password");
      
    }

    if (valid) {
      register();
    }
  };


  const register = () => {
    setLoading(true);
    fetch('http://192.168.0.163:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(inputs),
    }).then((res) => res.json())
    .then((data) => {
      setLoading(false);
      if (data.error) {
        Alert.alert("Error", data.error);
      } else {
        try {
          AsyncStorage.setItem("user", JSON.stringify(inputs));
        } catch (error) {
          Alert.alert("Error", 'Unable to access login page');
        }
        Alert.alert("Success", data.message);
        navigation.navigate('Login');
      }
    })
    .catch((err) => {
      setLoading(false);
      Alert.alert("Error", "Unable to access registration page");
      console.error(err);
    });
  };

    /*setTimeout(() => {
      setLoading(false);
      try {
        AsyncStorage.setItem("user", JSON.stringify(inputs));
        navigation.navigate('Login');
      } catch (error) {
        Alert.alert("Error", 'Unable to access login page');
      }
    }, 3000);
  }; */

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
          Register
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
            placeholder="Enter your fullname"
            iconName="account-outline"
            label="Fullname"
            error={errors.fullname}
            onFocus={() => {
              handleError(null, "fullname");
            }}
            onChangeText = {text => handleOnChange(text, "fullname")}
            // error="Please enter a valid username"
          />
          <Input 
            placeholder="Enter your username"
            iconName="account-outline"
            label="Username"
            error={errors.username}
            onFocus={() => {
              handleError(null, "username");
            }}
            onChangeText = {text => handleOnChange(text, "username")}
            // error="Please enter a valid username"
          />
          <Input
            keyboardType="numeric" 
            placeholder="Enter your phone number"
            iconName="phone-outline"
            label="Phone Number"
            error={errors.phone}
            onFocus={() => {
              handleError(null, "phone");
            }}
            onChangeText = {text => handleOnChange(text, "phone")}
            // error="Please enter a valid username"
          />
          <Input
            placeholder="Enter your Address"
            iconName="map-marker-outline"
            label="Address"
            error={errors.address}
            onFocus={() => {
              handleError(null, "address");
            }}
            onChangeText = {text => handleOnChange(text, "address")}
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
          <Button title="Register" onPress={validate}/>
          <Text 
            onPress={() => navigation.navigate("Login")}
            style={{color: COLORS.black,
            textAlign: 'center',
            fontWeight: 'bold',
          }}>
          Already have an account? Login
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

export default RegisterScreen;
