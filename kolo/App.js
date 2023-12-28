import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { MaterialIcons } from "@expo/vector-icons";

import TouchScreen from "./src/screens/TouchScreen";
import PinScreen from "./src/screens/PinScreen";
import DashBoard from "./src/screens/DashBoard";
import SendRequestScreen from "./src/screens/SendRequestScreen";
import CardsScreen from "./src/screens/CardsScreen";
import LoginScreen from "./src/screens/LoginScreen";
import RegisterScreen from "./src/screens/RegisterScreen";



const App = () => {
  const AppState = createStackNavigator();
  const TabStack = createBottomTabNavigator();


  const screenOptions = ({route}) => ({
    tabBarIcon: ({focused}) => {
      let icon = "";
      const color = focused ? "#559dff" : "#828282";
      const size = 24;
      
      switch (route.name) {
        case "Cards":
          icon = "credit-card";
          break;

        case "SendRequest":
          icon = "send";
          break;
          
        default:
          icon = "dashboard";
        }
        return <MaterialIcons name={icon} size={size} color={color} />;
      },
      tabBarOptions: {
        showLabel: true,
        style: {
          backgroundColor: "#1e1e1e",
          borderTopColor: "#1e1e1e",
          paddingBottom: 32,
        },
      },
    });


  const TabStackScreens = () => {
    return (
      <TabStack.Navigator screenOptions={screenOptions}>
        <TabStack.Screen name="Dashboard" component={DashBoard} />
        <TabStack.Screen 
          name="SendRequest"
          component={SendRequestScreen}
          options={{title: "Send & Request"}}
        />
        <TabStack.Screen name="Cards" component={CardsScreen} options={{ title: "My Cards" }} />
      </TabStack.Navigator>
    );
  }; 

  return (
    <NavigationContainer>
      <AppState.Navigator screenOptions={{ headerShown: false }}>
        <AppState.Screen name="Login" component={LoginScreen} />
        <AppState.Screen name="Touch" component={TouchScreen} />
        <AppState.Screen name="Pin" component={PinScreen} />
        <AppState.Screen name="Tabs" component={TabStackScreens} />
        <AppState.Screen name="Register" component={RegisterScreen} />
        <AppState.Screen name="DashBoard" component={DashBoard} />
      </AppState.Navigator>
    </NavigationContainer>
  );
};

export default App;
