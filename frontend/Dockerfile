# Frontend Dockerfile
# Multi-stage build for SvelteKit application

# Stage 1: Dependencies
FROM node:20-alpine as dependencies

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Stage 2: Development
FROM node:20-alpine as development

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy application code
COPY . .

# Expose port
EXPOSE 5173

# Development server
CMD ["pnpm", "run", "dev", "--", "--host", "0.0.0.0"]

# Stage 3: Build
FROM node:20-alpine as build

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy application code
COPY . .

# Build application
RUN pnpm run build

# Stage 4: Production
FROM node:20-alpine as production

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

# Install only production dependencies
RUN pnpm install --frozen-lockfile --prod

# Copy built application from build stage
COPY --from=build /app/build ./build
COPY --from=build /app/.svelte-kit ./.svelte-kit
COPY --from=build /app/static ./static

# Expose port
EXPOSE 5173

# Production preview server
CMD ["pnpm", "run", "preview", "--", "--host", "0.0.0.0"]

