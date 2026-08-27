from client import UnifiedStreamingAiGatewayFallbackRouterClient

def main():
    client = UnifiedStreamingAiGatewayFallbackRouterClient()
    res = client.route_streaming_completion({'messages': [{'role': 'user', 'content': 'Analyze cybersecurity log events'}]})
    print('AI Gateway Session: ' + res['routing_session_id'] + ' (Active: ' + res['active_provider'] + ')')
    print('Fallbacks: ' + ', '.join(res['fallback_providers_ready']) + ' | Circuit Breaker: ' + str(res['zero_latency_circuit_breaker_active']))
    print('Structured Stream: ' + str(res['structured_object_stream_validated']) + ' (P95 Latency: ' + str(res['roundtrip_latency_p95_ms']) + 'ms)')
    print('Proxy Endpoint: ' + res['gateway_proxy_url'])

if __name__ == '__main__':
    main()
