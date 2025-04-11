import React from 'react';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import ContactForm from './components/ContactForm';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <ContactForm />
    </ThemeProvider>
  );
}

export default App;
