import React, {useState} from 'react';
import { Text, View, Image, TextInput, StyleSheet, TouchableOpacity } from 'react-native';
import { Video } from 'expo-av';
// import CountryPicker from 'react-native-country-picker-modal';

const Registration = ({ navigation }) => {
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');

    const handleRegistrations = async () => {
        console.log('Registering Data:', {
            firstname,
            lastname,
            email,
            username,
        });

        navigation.navigate('Login');
    };
    return (
        <View style={styles.container}>
            <Video
                source={require('./assets/videos/vid.mp4')}
                style={styles.backgroundVideo}
                isMuted={false}
                resizeMode="cover"
                shouldPlay
                isLooping
            />
            
            <Image source={require('./assets/kolo.png')} style={styles.logo} />
            <View style={styles.overlay}>
                <Text style={styles.title}>Registration</Text>
                <TextInput
                    style={styles.input}
                    placeholder="Username"
                    value={username}
                    onChangeText={(text) => setUsername(text)}
                />
                <TextInput
                    style={styles.input}
                    placeholder="First Name"
                    value={firstname}
                    onChangeText={(text) => setFirstname(text)}
                />
                <TextInput
                    style={styles.input}
                    placeholder="Last Name"
                    value={lastname}
                    onChangeText={(text) => setLastname(text)}
                />
                <TextInput
                    style={styles.input}
                    placeholder="Email"
                    value={email}
                    onChangeText={(text) => setEmail(text)}
                />    

                <TouchableOpacity onPress={() => navigation.navigate('NextPage')}>
                    <Text style={styles.nextLink}>Next {'>'} </Text>
                </TouchableOpacity>
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
    },
    backgroundVideo: {
      position: 'absolute',
      top: 0,
      left: 0,
      bottom: 0,
      right: 0,
    },
    logo: {
        position: 'absolute',
        top: 25,
        left: 0,
        width: 70,
        height: 70,
        resizeMode: 'cover',
        opacity: 0.8,
        zIndex: 1,
    },
    overlay: {
      ...StyleSheet.absoluteFillObject,
      justifyContent: 'center',
      alignItems: 'center',
    },
    title: {
      fontSize: 20,
      fontWeight: 'bold',
      textAlign: 'center',
      margin: 10,
      color: 'black',
    },
    input: {
      width: 200,
      height: 40,
      margin: 10,
      borderWidth: 1,
      borderColor: 'blue',
      borderRadius: 5,
      backgroundColor: '#CCCDF9',
      padding: 10,
      shadowColor: 'white',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.2,
      shadowRadius: 3,
    },
    nextLink: {
        color: 'purple',
        marginTop: 40,
        textAlign: 'right',
      },
  });

export default Registration;
