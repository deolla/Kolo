import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";


import TouchScreen from "./src/screens/TouchScreen";
import PinScreen from "./src/screens/PinScreen";

const App = () => {
  const AppState = createStackNavigator();

  return (
    <NavigationContainer>
      <AppState.Navigator screenOptions={{ headerShown: false }}>
        <AppState.Screen name="Touch" component={TouchScreen} />
        <AppState.Screen name="Pin" component={PinScreen} />
      </AppState.Navigator>
    </NavigationContainer>
  );
};

export default App;
