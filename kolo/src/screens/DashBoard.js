import React from 'react';
import styled from 'styled-components';
import {FontAwesome5, MaterialIcons, AntDesign} from '@expo/vector-icons';
import { StatusBar } from 'expo-status-bar';

import Text from '../components/Text';


export default DashBoardScreen = () => {
  return (
    <Container>
      <Header>
        <ProfilePhoto source={require('../../assets/profile_pic.jpg') } />
        <Welcome>
          <Text heavy medium >Welcome,</Text>
          <Text>DesignIntoCode</Text>
        </Welcome>
        <FontAwesome5 name="cog" size={24} color="#565656" />
      </Header>

      <Text center title black>
        $9, 156.18
      </Text>
      <Text center heavy color="#727479">
        Current Balance
      </Text>

      <Purchases ListHeaderComponent= {
        <>
          <TransactionHeader>
            <Text>Last Purchases</Text>
            <MaterialIcons name="sort" size={24}  color="#5196f4" />
          </TransactionHeader>

          <SearchContainer>
              <AntDesign name="search1" size={18} color="#5196f4" />
              <Search placeHolder="Search Transactions" />
          </SearchContainer>
        </>
      } 
      />

      <StatusBar barStyle="light-content" />
    </Container>
  );
};

const Container = styled.SafeAreaView`
  flex: 1;
  background-color: #1e1e1e;
`;

const Header = styled.View`
  flex-direction: row;
  align-items: center;
  margin: 16px 16px 32px 16px;
`;

const ProfilePhoto = styled.Image`
  width: 44px;
  height: 44px;
  border-radius: 22px;

`;

const Welcome = styled.View`
  flex: 1;
  padding: 0 16px;
`;

const Purchases = styled.FlatList`
  background-color: #2c2c2c;
  padding: 16px;

`;

const TransactionHeader = styled.View`
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
`;

const SearchContainer = styled.View`
  background-color: #3d3d3d;
  flex-direction: row;
  align-items: center;
  padding: 0 8px;
  border-radius: 6px;
  margin: 16px 0;
`;

const Search = styled.TextInput`
  flex: 1;
  padding: 8px 16px;
  font-family: "Helvetica Neue, Helvetica, Arial, sans-serif";
  color: #dbdbdb;

`;

// const StatusBar = styled.StatusBar``;
