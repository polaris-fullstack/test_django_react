import React, { useState } from 'react';
import axios from 'axios';
import {
  Box,
  Button,
  TextField,
  Typography,
  Container,
  Alert,
} from '@mui/material';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    phone_number: '',
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess(false);

    try {
      await axios.post('http://localhost:8000/api/contacts/', formData);
      setSuccess(true);
      setFormData({
        first_name: '',
        last_name: '',
        phone_number: '',
      });
    } catch (err) {
      setError(err.response?.data?.message || 'An error occurred while submitting the form');
    }
  };

  return (
    <Container maxWidth="sm">
      <Box
        component="form"
        onSubmit={handleSubmit}
        sx={{
          mt: 4,
          display: 'flex',
          flexDirection: 'column',
          gap: 2,
        }}
      >
        <Typography variant="h4" component="h1" gutterBottom>
          Contact Form
        </Typography>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        {success && (
          <Alert severity="success" sx={{ mb: 2 }}>
            Contact information submitted successfully!
          </Alert>
        )}

        <TextField
          required
          fullWidth
          label="First Name"
          name="first_name"
          value={formData.first_name}
          onChange={handleChange}
          margin="normal"
        />

        <TextField
          required
          fullWidth
          label="Last Name"
          name="last_name"
          value={formData.last_name}
          onChange={handleChange}
          margin="normal"
        />

        <TextField
          required
          fullWidth
          label="Phone Number"
          name="phone_number"
          value={formData.phone_number}
          onChange={handleChange}
          margin="normal"
        />

        <Button
          type="submit"
          variant="contained"
          color="primary"
          size="large"
          sx={{ mt: 2 }}
        >
          Submit
        </Button>
      </Box>
    </Container>
  );
};

export default ContactForm; 