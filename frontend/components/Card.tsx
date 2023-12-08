import {
  Card,
  CardBody,
  CardFooter,
  Heading,
  Stack,
  Text,
  Button,
  Box,
} from "@chakra-ui/react";

export default function RecommendationCard({
  title,
  level,
  category,
  ingredients,
}: {
  title: string;
  level: string;
  category: string;
  ingredients: string;
}) {
  return (
    <Card
      direction={{ base: "column", sm: "row" }}
      overflow="hidden"
      variant="outline"
    >
      <Stack>
        <CardBody>
          <Heading size="md">title</Heading>

          <Text py="2">{ingredients}</Text>
        </CardBody>

        <CardFooter>
          <Button as={"a"} variant={"link"} href="/order" colorScheme="blue">
            Order
          </Button>
        </CardFooter>
      </Stack>
    </Card>
  );
}
