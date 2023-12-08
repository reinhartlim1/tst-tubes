'use client'
import React, { useState } from 'react';
import { Button, VStack, Flex, Box, Heading, Text, Grid, FormControl, Card, CardBody, Input } from '@chakra-ui/react';
import RecommendationCard from '@/components/Card'
import Sidebar from "@/components/SideBar";

export default function Page() {
  return (
    <Flex>
      <Sidebar />
      <Box w="100%" pl="20">
        <Heading pt="10">
        Recommendation
        </Heading>
        <Grid templateColumns="repeat(2, 1fr)" gap={6}>
        <Box>
        <Text pt="5" pb="3">
          Recommendation by Order History
        </Text>
        <Button w="90%"> Get all the recipes</Button>
        <Card mt="5" w="90%" bg="gray.100" h="36">
          <CardBody>
            <Text fontWeight="bold">Judul Recipe</Text>
            <Text fontSize="xs">Ingredients</Text>
          </CardBody>
        </Card>
        </Box>
        <Box>
        <Text pt="5" pb="3">
          Recommendation by ID
        </Text>
        <Flex>
        <FormControl w="60%">
          <Input placeholder = "ID" type="number" />
        </FormControl>
        <Box pl="2">
        <Button px="60%"> Get </Button>
        </Box>
        </Flex>
        <Card mt="5" w="90%" bg="gray.100" h="36">
          <CardBody>
            <Text fontWeight="bold">Judul Recipe</Text>
            <Text fontSize="xs">Ingredients</Text>
          </CardBody>
        </Card>
        </Box>
        </Grid>
      </Box>
    </Flex>
  );
};