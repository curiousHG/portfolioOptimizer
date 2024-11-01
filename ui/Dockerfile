# Use an official Node.js runtime as a parent image
FROM node:23-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the Next.js application
RUN npm run build

# --- Production Image ---
FROM node:23-alpine

# Set working directory
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/next.config.mjs ./next.config.mjs

# Set environment variable to production
ENV NODE_ENV production

# Expose the port Next.js will run on
EXPOSE 3000

# Start the Next.js application
CMD ["npm", "start"]
