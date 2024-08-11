import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.welcomeText}>
        <Text style={styles.welcomeToText}>Welcome to </Text>
        <Text style={styles.farmVitalsText}>FarmVitals</Text>
      </Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#000000",
    alignItems: "center",
    justifyContent: "center",
  },
  welcomeText: {
    fontFamily: "Poppins",
  },
  welcomeToText: {
    color: "#4AAF54",
    fontWeight: "500",
    fontSize: 21,
  },
  farmVitalsText: {
    color: "#4AAF54",
    fontWeight: "800",
    fontSize: 26,
  },
});
